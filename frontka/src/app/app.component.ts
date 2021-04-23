import {Component, OnInit} from '@angular/core';
import {ToursService} from './tours.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Tour';
  logged = false;
  username = '';
  password = '';

  // tslint:disable-next-line:typedef use-lifecycle-interface
  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }
  constructor(private toursService: ToursService) {}
  // tslint:disable-next-line:typedef
  login() {
    this.toursService.login(this.username, this.password).subscribe((data) => {

      localStorage.setItem('token', data.token);
      this.logged = true;
      this.username = '';
      this.password = '';
    });
  }
  // tslint:disable-next-line:typedef
  logout() {
    this.logged = false;
    localStorage.removeItem('token');
  }
}



