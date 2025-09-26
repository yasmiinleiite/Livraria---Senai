import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AutoresPage } from './pages/authors/authors.component';
import { PublisherPage } from './pages/publisher/publisher.component';

export const routes: Routes = [
    {path: '', component: HomeComponent},
    {path: 'home', component: HomeComponent},
    {path: 'autores', component: AutoresPage},
    {path: 'editoras', component: PublisherPage}
];
