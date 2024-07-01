import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ProductService } from '../../services/product.services';
import { EditProductModules } from './edit.product.modules';

//import { AppModule } from '../../../app.module';

@Component({
  selector: 'app-edit-product',
  templateUrl: './edit.product.component.html',
  styleUrls: ['./edit.product.component.css']
})
export class EditProductComponent implements OnInit {
  productId!: string;
  product: any = {}; // Objeto para armazenar dados do produto

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private productService: ProductService
  ) { }

  ngOnInit(): void {
    this.productId = this.route.snapshot.params['id']; // Captura o parâmetro ':id' da rota
    this.loadProductDetails();
  }

  loadProductDetails() {
    this.productService.getProductById(this.productId).subscribe(
      (data) => {
        this.product = data; // Preenche o objeto 'product' com os detalhes do produto
      },
      (error) => {
        console.error('Erro ao carregar detalhes do produto:', error);
      }
    );
  }

  updateProduct() {
    this.productService.updateProduct(this.productId, this.product).subscribe(
      () => {
        console.log('Produto atualizado com sucesso.');
        this.router.navigate(['/list-products']); // Redireciona de volta para a lista de produtos após a atualização
      },
      (error) => {
        console.error('Erro ao atualizar produto:', error);
      }
    );
  }
}
