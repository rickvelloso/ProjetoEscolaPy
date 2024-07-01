import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';

import { routes } from './app/app.routes';
import { AppRoutingModule } from './app/app-routing.module';
import { AppComponent } from './app/app.component';
import { HomeComponent } from './app/components/home/home.component';
import { ProductComponent } from './app/components/product/product.components';
import { ListProductsModule } from './app/components/list-products/list.products.module';
import { CreateProductModule } from './app/components/create-product/create.product.modules'; // Corrigido para .module
import { EditProductComponent } from './app/components/edit-product/edit.product';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ProductComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot(routes),
    FormsModule,
    AppRoutingModule,
  EditProductComponent,
    ListProductsModule, // Importado corretamente como módulo
    CreateProductModule // Importado corretamente como módulo
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
