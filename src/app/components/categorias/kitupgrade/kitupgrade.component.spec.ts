import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { KitupgradeComponent } from './kitupgrade.component';

describe('KitupgradeComponent', () => {
  let component: KitupgradeComponent;
  let fixture: ComponentFixture<KitupgradeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ KitupgradeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(KitupgradeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
