import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Autor } from '../models/autor';
import { environment } from '../../environments/environments';

@Injectable({ providedIn: 'root' })
export class AutoresService {
  private http = inject(HttpClient);
  private base = environment.apiBase;
  
  listar(): Observable<Autor[]> {
    const url = `${this.base}api/autores/`;
    return this.http.get<Autor[]>(url);
  }
}
