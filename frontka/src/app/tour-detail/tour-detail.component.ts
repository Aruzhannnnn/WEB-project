import { Component, OnInit } from '@angular/core';
import {Tour} from '../models';
import {ActivatedRoute} from '@angular/router';
import {TOURS} from '../tours';
import {ToursService} from '../tours.service';
import {Location} from '@angular/common';


@Component({
  selector: 'app-tour-detail',
  templateUrl: './tour-detail.component.html',
  styleUrls: ['./tour-detail.component.css']
})
export class TourDetailComponent implements OnInit {
  tour ?: Tour;

  constructor(private route: ActivatedRoute,
              private location: Location,
              private toursService: ToursService) {

  }

  ngOnInit(): void {
    // this.getRecipe();
    const routeParams = this.route.snapshot.paramMap;
    const IdFromRoute = Number(routeParams.get('id'));
    this.tour = TOURS.find(tour => tour.id === IdFromRoute);
  }

  goBack(): void {
    this.location.back();
  }
}
