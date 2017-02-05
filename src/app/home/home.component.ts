import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html'
})
export class HomeComponent {

  title: string;
  currentUrl: string;

  constructor(private router: Router ) {
    // On route change
    this.router.events.subscribe(path => {
      this.currentUrl = path.url;
      // Billing info
      if (this.currentUrl == '/journal') {
        this.title = "Journal";
      // Scent Profile
      } else if (this.currentUrl == '/insights') {
        this.title = "Insights";
      }
    });
  }
}
