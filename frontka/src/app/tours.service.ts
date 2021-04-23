import {Injectable} from '@angular/core';
import {TOURS} from './tours';
import {HttpClient} from '@angular/common/http';
import {Observable, of} from 'rxjs';
import {MessageService} from './message.service';
import {AuthToken, Tour} from './models';


@Injectable({
  providedIn: 'root'
})
export class ToursService {
  // tslint:disable-next-line:variable-name
  BASE_URl = 'http://localhost:8000';

  constructor(private messageService: MessageService, private http: HttpClient) {
  }

  login(username, password): Observable<AuthToken>{
    return this.http.post<AuthToken>(`${this.BASE_URl}/api/login/`,  {
      username,
      password
   });
  }
  getTours(): Observable<Tour[]> {
    const tours = of(TOURS);
    this.messageService.add('ToursService: fetched tours');
    return tours;
  }

}
