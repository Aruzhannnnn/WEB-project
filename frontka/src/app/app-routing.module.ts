import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { NotFoundComponent } from './not-found/not-found.component';
import {ToursComponent} from './tours/tours.component';
import {TourDetailComponent} from './tour-detail/tour-detail.component';
import {LoginComponent} from './login/login.component';
import {DemoComponent} from './demo/demo.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'tours', component: ToursComponent},
  { path: 'tours/:id', component: TourDetailComponent},
  { path: 'login', component: LoginComponent },
  { path: 'demo', component: DemoComponent},
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: '**', component: NotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
