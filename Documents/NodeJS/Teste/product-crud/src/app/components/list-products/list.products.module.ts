import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ListProductsComponent } from './list.products';

@NgModule({
  declarations: [
    ListProductsComponent
  ],
  imports: [
    CommonModule,
    FormsModule
  ],
  exports: [
    ListProductsComponent
  ]
})
export class ListProductsModule { }
