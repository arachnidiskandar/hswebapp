import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filtrocategoria'
})
export class FiltrocategoriaPipe implements PipeTransform {

  transform(value: any, ...args: any[]): any {
    return null;
  }

}
