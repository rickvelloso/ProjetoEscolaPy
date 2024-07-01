import { Component } from '@angular/core';
import { ProductService } from '../../services/product.services';
import { CreateProductModule } from './create.product.modules';

@Component({
  selector: 'app-create-product',
  templateUrl: './create.product.component.html',
  styleUrls: ['./create.product.component.css']
})
export class CreateProductComponent {
  newProduct = { name: '', price: 0, quantity: 0 };

  constructor(private productService: ProductService) {}

  async addProduct() {
    await this.productService.createProduct(this.newProduct).toPromise();
    this.newProduct = { name: '', price: 0, quantity: 0 };
  }
}
