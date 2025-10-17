import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { LivrosService } from '../../services/livros.services';
import { Livro } from '../../models/livro';
import { AuthService } from '../../services/auth.services';
import { environment } from '../../../environments/environments';

@Component({
  selector: 'app-books',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './books.component.html',
})
export class BooksComponent {
  private svc = inject(LivrosService);
  private auth = inject(AuthService);

  livros = signal<Livro[]>([]);
  carregando = signal(true);
  erro = signal<string | null>(null);

  apiBase = (environment.apiBase ?? '').replace(/\/+$/, '');

  // controle local de upload
  private pendentes = new Map<number, File>();
  private previews = new Map<number, string>();
  private upStatus = new Map<number, 'idle' | 'up' | 'ok' | 'err'>();

  constructor() {
    console.log('Token de acesso:', this.auth.token());

    // Carregar lista inicial de livros
    this.svc.listar({ ordering: 'titulo' }).subscribe({
      next: (data) => {
        this.livros.set(data);
        this.carregando.set(false);
      },
      error: () => {
        this.erro.set('Falha ao carregar livros');
        this.carregando.set(false);
      },
    });
  }

  /** Retorna o id único para o input file */
  fileInputId(id: number): string {
    return `file-capa-${id}`;
  }

  /** Retorna a URL da capa do livro (preview local ou do servidor) */
  capaSrc(l: Partial<Livro> & { id?: number }): string | null {
    const lid = Number(l?.id ?? (l as any)?.pk ?? -1);
    const prv = this.previews.get(lid);
    if (prv) return prv;

    const anyL = l as any;
    if (anyL?.capa_url) return String(anyL.capa_url);

    if (l.capa) {
      const rel = String(l.capa);
      const path = rel.startsWith('/media/') ? rel : `/media/${rel}`;
      return `${this.apiBase}${path}`;
    }
    return null;
  }

  /** Retorna o status do upload de um livro */
  statusUpload(id: number): 'idle' | 'up' | 'ok' | 'err' {
    return this.upStatus.get(id) ?? 'idle';
  }

  /** Ao selecionar uma nova capa */
  async onSelect(e: Event, id: number) {
    const file = (e.target as HTMLInputElement).files?.[0];
    if (!file) return;

    // Criar preview local
    const url = URL.createObjectURL(file);
    const old = this.previews.get(id) || null;
    this.previews.set(id, url);
    this.pendentes.set(id, file);
    this.upStatus.set(id, 'up');

    // Enviar para o backend (PATCH /api/livro/:id/)
    this.svc.enviarCapa(id, file).subscribe({
      next: (livroAtualizado) => {
        // Atualiza a lista com o retorno do servidor
        this.livros.update((arr) =>
          arr.map((l) =>
            Number((l as any).id ?? (l as any).pk) === id
              ? livroAtualizado
              : l
          )
        );

        this.upStatus.set(id, 'ok');
        this.pendentes.delete(id);

        // Revogar preview temporário
        setTimeout(() => {
          const u = this.previews.get(id);
          if (u && u.startsWith('blob:')) URL.revokeObjectURL(u);
          this.previews.delete(id);
        }, 500);
      },
      error: (err) => {
        console.error(err);
        this.upStatus.set(id, 'err');

        // Restaurar preview anterior
        const u = this.previews.get(id);
        if (u && u.startsWith('blob:')) URL.revokeObjectURL(u);
        if (old) this.previews.set(id, old);
        else this.previews.delete(id);

        this.erro.set('Falha ao enviar capa');
      },
    });
  }
}
