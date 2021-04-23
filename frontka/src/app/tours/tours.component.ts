import { Component, OnInit } from '@angular/core';
import {Tour} from '../models';
import {ToursService} from '../tours.service';
import {TOURS} from '../tours';
import {MessageService} from '../message.service';


@Component({
  selector: 'app-tours',
  templateUrl: './tours.component.html',
  styleUrls: ['./tours.component.css']
})
export class ToursComponent implements OnInit {
  tours: Tour[] = [];
  constructor(private toursService: ToursService,
              private messageService: MessageService) {
  }

  ngOnInit(): void {
    this.tours = TOURS;
  }

  getTours(): void {
    this.toursService.getTours().subscribe(tours => this.tours = tours);
  }

  // tslint:disable-next-line:typedef
  likeItem(id: number) {
    this.tours[id].like += 1;
  }

  // tslint:disable-next-line:ban-types typedef
  share(link: String, text: String) {
    window.open('https://telegram.me/share/url?url=' + link, '_blank');
  }

  removeItem(id: number): void {
    this.tours = this.tours.filter(x => x.id !== id);
  }

}
