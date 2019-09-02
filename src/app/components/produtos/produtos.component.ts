import { ProdutoComponent } from './../produto/produto.component';
import { Component, OnInit } from '@angular/core';
import { PRODUTOS } from '../../mock-produtos';
@Component({
  selector: 'app-produtos',
  templateUrl: './produtos.component.html',
  styleUrls: ['./produtos.component.css']
})
export class ProdutosComponent implements OnInit {
  listaProdutos = PRODUTOS;
  qntdProdutosPagina: number;

  constructor() { }

  ngOnInit() {
    this.qntdProdutosPagina = this.listaProdutos.length;
  }

}
