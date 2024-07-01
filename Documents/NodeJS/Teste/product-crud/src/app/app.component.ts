import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'product-crud';

  constructor(private router: Router) {}

  navigateToCreateProduct() {
    this.router.navigate(['/create-product']);
  }

  navigateToListProducts() {
    this.router.navigate(['/list-products']);
  }
}
