import { Produto } from './Produto';
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filter'
})
export class FilterPipe implements PipeTransform {

  transform(items: any[], textoDigitado: string): any {
    if (!items || !textoDigitado) {
      return items;
  }
  textoDigitado = textoDigitado.toLowerCase();
  // filter items array, items which match and return true will be
  // kept, false will be filtered out
  return items.filter(item => item.nomeProduto.indexOf(textoDigitado) !== -1);
  }
}
