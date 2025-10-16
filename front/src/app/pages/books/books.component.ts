import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { LivrosService } from '../../services/livros.services';
import { Livro } from '../../models/livro';
import { AuthService } from '../../services/auth.services';
import { environment } from '../../../environments/environments';

@Component({
  selector: 'app-books.component',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.css'],
})
export class BooksComponent {
  private svc = inject(LivrosService);
  private auth = inject(AuthService);

  livros = signal<Livro[]>([]);
  carregando = signal(true);
  erro = signal<string | null>(null);

  apiBase = (environment.apiBase ?? '').replace(/\/+$/, '');

  // arquivos selecionados (pendentes de upload)
  private pendentes = new Map<number, File>();
  // previews por livro (ObjectURL)
  private previews = new Map<number, string>();
  // status de upload por livro
  private upStatus = new Map<number, 'idle' | 'up' | 'ok' | 'err'>();

  constructor() {
    console.log('Token de acesso: ', this.auth.token());
    this.svc.listar().subscribe({
      next: (data) => { this.livros.set(data); this.carregando.set(false); },
      error: () => { this.erro.set('Falha ao carregar livros'); this.carregando.set(false); }
    });
  }
}
