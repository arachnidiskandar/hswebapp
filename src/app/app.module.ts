
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { ProdutosComponent } from './components/produtos/produtos.component';
import { FilterPipe } from './pipes/filtroProdutos/filter.pipe';
import { AppRoutingModule } from './app-routing.module';
import { TelatesteComponent } from './components/telateste/telateste.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    ProdutosComponent,
    FilterPipe,
    TelatesteComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
