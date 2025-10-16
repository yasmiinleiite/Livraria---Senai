import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImagemService, Imagem } from '../../services/imagens.service';
import { environment } from '../../../environments/environments.prod';

@Component({
  standalone: true,
  selector: 'app-imagens',
  imports: [CommonModule],
  templateUrl: './images.component.html',
})
export class ImagensComponent {
  private svc = inject(ImagemService);
  imagens = signal<Imagem[]>([]);
  status = '';
  arquivo: File | null = null;
  preview: string | null = null;
  apiBase = environment.apiBase

  // constructor() {
  //   // ajuste se quiser compor url absoluta manualmente
  //   const base = (window as any).ENV_API_BASE ?? '';
  //   this.apiBase = base.replace(/\/+$/,'').replace(/\/api$/,'') || 'http://127.0.0.1:8000';

  //   this.carregar();
  // }

  carregar() {
    this.svc.listar().subscribe({
      next: (data: any) => {
        // Se sua API estiver paginando, use data.results
        this.imagens.set(Array.isArray(data) ? data : data.results ?? []);
      },
      error: () => this.status = 'Falha ao carregar imagens.'
    });
  }

  onFile(e: Event) {
    const input = e.target as HTMLInputElement;
    this.arquivo = input.files?.[0] ?? null;

    if (this.arquivo) {
      const reader = new FileReader();
      reader.onload = () => this.preview = reader.result as string;
      reader.readAsDataURL(this.arquivo);
    } else {
      this.preview = null;
    }
  }

  onSubmit(ev: Event) {
    ev.preventDefault();
    if (!this.arquivo) return;
    this.status = 'Enviando...';

    this.svc.enviar(this.arquivo).subscribe({
      next: (img) => {
        this.status = 'Imagem enviada.';
        this.arquivo = null;
        this.preview = null;
        this.imagens.update((arr) => [img, ...arr]);
      },
      error: (err) => {
        console.error(err);
        this.status = 'Falha ao enviar.';
      }
    });
  }

  remover(id: number) {
    this.svc.deletar(id).subscribe({
      next: () => this.imagens.update((arr) => arr.filter(i => i.id !== id)),
      error: () => this.status = 'Falha ao remover.'
    });
  }
}
