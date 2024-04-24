import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsersService {
  baseUrl = 'http://127.0.0.1:8000'; // Обновите URL в зависимости от вашего конфига

  constructor(private http: HttpClient) { }

  register(user: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/register/`, user);
  }

  getProfile(): Observable<any> {
    return this.http.get(`${this.baseUrl}/profile/`);
  }
}
