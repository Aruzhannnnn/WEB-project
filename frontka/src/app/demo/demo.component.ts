import {Component, OnInit} from '@angular/core';
import {ToursService} from '../tours.service';

@Component({
  selector: 'app-demo',
  templateUrl: './demo.component.html',
  styleUrls: ['./demo.component.css']
})
export class DemoComponent implements OnInit {
  title = 'demo-front';

  logged = false;
  username = '';
  password = '';

  // tslint:disable-next-line:typedef
  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }

  constructor(private toursService: ToursService) {
  }

  // tslint:disable-next-line:typedef
  login() {
    alert('Success!');
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
