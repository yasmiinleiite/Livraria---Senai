import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AutoresPage } from './pages/authors/authors.component';
import { PublisherComponent } from './pages/publisher/publisher.component';
import { BooksComponent } from './pages/books/books.component';
import { LoginComponent } from './pages/login/login.component';
import { authGuard } from './auth.guard';

export const routes: Routes = [
    {path: '', component: LoginComponent},
    {path: 'login', component: LoginComponent},
    {path: 'home', component: HomeComponent},
    {path: 'autores', component: AutoresPage, canActivate: [authGuard]},
    {path: 'editoras', component: PublisherComponent, canActivate: [authGuard]},
    {path: 'livros', component: BooksComponent, canActivate: [authGuard]}
];
