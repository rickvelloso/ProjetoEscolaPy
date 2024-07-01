import { Component, OnInit } from '@angular/core';
import { ProductService } from '../../services/product.services';
import { ListProductsModule } from './list.products.module';
import { Router } from '@angular/router';

@Component({
  selector: 'app-list-products',
  templateUrl: './list.products.component.html',
  styleUrls: ['./list.products.component.css']
})
export class ListProductsComponent implements OnInit {
  products: any[] = [];
  searchTerm: string = '';
  filteredProducts: any[] = [];

  constructor(private productService: ProductService, private router: Router) {}

  ngOnInit(): void {
    this.loadProducts();
  }

  async loadProducts() {
    try {
      this.products = await this.productService.getProducts().toPromise() || [];
      this.filteredProducts = this.products; // Inicializa o filtro com todos os produtos
    } catch (error) {
      console.error('Erro ao carregar produtos:', error);
    }
  }

  async deleteProduct(id: string) {
    try {
      await this.productService.deleteProduct(id).toPromise();
      this.loadProducts();
    } catch (error) {
      console.error('Erro ao deletar produto:', error);
    }
  }

  updateProduct(id: string) {
    this.router.navigate(['/edit-product', id]);
  }

  applyFilter() {
    if (!this.searchTerm) {
      this.filteredProducts = [...this.products]; // Se searchTerm estiver vazio, exibe todos os produtos
      return;
    }

    this.filteredProducts = this.products.filter((product) =>
      product.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );
  }
}
