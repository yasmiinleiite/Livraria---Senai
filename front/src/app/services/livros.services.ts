// livros.sevices.ts  (confira o nome do arquivo; muitas vezes escrevem "services")
import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environments';
import { Livro } from '../models/livro';

export type LivroQuery = {
  search?: string;
  titulo?: string;
  autor?: string;
  id?: number | string;
  ordering?: string; // ex.: 'titulo' | '-titulo'
};

@Injectable({ providedIn: 'root' })
export class LivrosService {
  private http = inject(HttpClient);
  private api = (environment.apiBase ?? '').replace(/\/+$/, '');

  // suas rotas CBV:
  private baseList = `${this.api}/api/livros`;   // sem barra final
  private baseDetail = `${this.api}/api/livro`;  // singular

  listar(q?: LivroQuery): Observable<Livro[]> {
    let params = new HttpParams();
    if (q) {
      for (const [k, v] of Object.entries(q)) {
        if (v !== undefined && v !== null && String(v).trim() !== '') {
          params = params.set(k, String(v));
        }
      }
    }
    return this.http.get<Livro[]>(this.baseList, { params });
  }

  enviarCapa(id: number, file: File) {
    const form = new FormData();
    form.append('capa', file);
    // detalhe SINGULAR + barra no final
    return this.http.patch<Livro>(`${this.baseDetail}/${id}/`, form);
  }
}
