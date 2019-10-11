import { Component, OnInit } from '@angular/core';
import { PRODUTOS } from '../../mock-produtos';
@Component({
  selector: 'app-produtos',
  templateUrl: './produtos.component.html',
  styleUrls: ['./produtos.component.css']
})
export class ProdutosComponent implements OnInit {
  listaProdutos = PRODUTOS;
  textoDigitado: string
  categoriaSelecionada: string;
  constructor() { }

  ngOnInit() {
  }
  limparFiltros() {
    this.categoriaSelecionada = '';
    this.textoDigitado = '';
  }
}
