

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { ProdutosComponent } from './components/produtos/produtos.component';
import { FilterPipe } from './pipes/filtroProdutos/filter.pipe';
import { AppRoutingModule } from './app-routing.module';
import { TelatesteComponent } from './components/telateste/telateste.component';
import { AngularFireModule } from '@angular/fire';
import { AngularFireDatabaseModule } from '@angular/fire/database';
import { environment } from './../environments/environment';

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
    AppRoutingModule,
    AngularFireModule.initializeApp(environment.firebaseConfig),
    AngularFireDatabaseModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
