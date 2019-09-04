import { ProdutosComponent } from './components/produtos/produtos.component';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';

import { TelatesteComponent } from './components/telateste/telateste.component';
const routes = [
  { path: '', redirectTo: '/produtos', pathMatch: 'full' },
  { path: 'outratela', component: TelatesteComponent },
  { path: 'produtos', component: ProdutosComponent }

]

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
