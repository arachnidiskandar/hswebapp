import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-produto',
  templateUrl: './produto.component.html',
  styleUrls: ['./produto.component.css']
})
export class ProdutoComponent implements OnInit {
  nome: string;
  descricacao: string;
  preco: number;
  categorias: string[];

  constructor() { }

  ngOnInit() {
  }

}
