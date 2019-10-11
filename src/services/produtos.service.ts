import { Injectable } from '@angular/core';
import { AngularFireDatabase } from '@angular/fire/database';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProdutosService {

  private produtosSource = new BehaviorSubject({ funcionario: null, key:''});
  funcionarioAtual = this.produtosSource.asObservable();

  constructor(private _angularFireDatabase: AngularFireDatabase) { }

  getAll() {


  }
}
