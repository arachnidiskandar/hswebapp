import { Produto } from '../../Produto';
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filter'
})
export class FilterPipe implements PipeTransform {

  transform(items: any[], textoDigitado: string, opcao: string): any {
    if (!items || !textoDigitado && !opcao) {
      return items;
    }
    else {
      if (opcao && !textoDigitado) { //Categoria selecionada, texto vazio
        return items.filter(item => item.categoria.toLowerCase() === opcao.toLowerCase());
      }
      else if (!opcao && textoDigitado) {//categoria vazia, texto digitado
        return items.filter(item => item.nomeProduto.toLowerCase().indexOf(textoDigitado.toLowerCase()) !== -1);
      }
      else {//categoria selecionada, texto digitado
        let itensFiltrados = items.filter(item => item.categoria.toLowerCase() === opcao.toLowerCase());
        return itensFiltrados.filter(item => item.nomeProduto.toLowerCase().indexOf(textoDigitado.toLowerCase()) !== -1);
      }
    }
  }
}
