import { Produto } from '../../Produto';
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filter'
})
export class FilterPipe implements PipeTransform {

  transform(items: any[], textoDigitado: string): any {
    if (!items || !textoDigitado) {
      return items;
  }
  // filtra os produtos pelo oq o cara digitou
  return items.filter(item => item.nomeProduto.toLowerCase().indexOf(textoDigitado.toLowerCase()) !== -1);
  }
}
