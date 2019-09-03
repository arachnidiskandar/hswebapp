import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-produto',
  templateUrl: './produto.component.html',
  styleUrls: ['./produto.component.css']
})
export class ProdutoComponent implements OnInit {
  nomeProduto: string;
  preçoAntigo: string;
  preçoNovo: string;
  preçoVista: string;
  linkImg: string;
  categoria: string;

  constructor() { }

  ngOnInit() {
  }

}
