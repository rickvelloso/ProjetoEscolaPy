import { Component, OnInit } from '@angular/core';
import { ProductService } from '../../services/product.services';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {
  products: any[] = []; // Inicializando como um array vazio
  newProduct = { name: '', price: 0, quantity: 0 };

  constructor(private productService: ProductService) {}

  ngOnInit(): void {
    this.loadProducts();
  }

  async loadProducts() {
    this.products = await this.productService.getProducts().toPromise() || []; // Tratamento para evitar undefined
  }

  async addProduct() {
    await this.productService.createProduct(this.newProduct).toPromise();
    this.newProduct = { name: '', price: 0, quantity: 0 };
    this.loadProducts();
  }

  async deleteProduct(id: string) {
    await this.productService.deleteProduct(id).toPromise();
    this.loadProducts();
  }
}
