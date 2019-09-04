
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { ProdutosComponent } from './components/produtos/produtos.component';
import { FilterPipe } from './pipes/filtroProdutos/filter.pipe';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    ProdutosComponent,
    FilterPipe
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
