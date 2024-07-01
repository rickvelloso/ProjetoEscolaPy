import { Routes } from '@angular/router';
import { CreateProductComponent } from './components/create-product/create.product';
import { ListProductsComponent } from './components/list-products/list.products';
import { EditProductComponent } from './components/edit-product/edit.product';
export const routes: Routes = [
  { path: 'create-product', component: CreateProductComponent },
  { path: 'list-products', component: ListProductsComponent },
  { path: 'edit-product/:id', component: EditProductComponent},
  { path: '**', redirectTo: '', pathMatch: 'full' }
];
