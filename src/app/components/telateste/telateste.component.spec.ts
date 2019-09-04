import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TelatesteComponent } from './telateste.component';

describe('TelatesteComponent', () => {
  let component: TelatesteComponent;
  let fixture: ComponentFixture<TelatesteComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TelatesteComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TelatesteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
