import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {environment} from '../../environments/environment.local';

/**
 * Api is a generic REST Api handler. Set your API url first.
 */
@Injectable()
export class Api {
  url = environment.apiUrl;
  headers;

  constructor(public http: HttpClient) {
    this.headers = new HttpHeaders();
    this.headers.set('X-CSRFToken', '**');
  }

  get(endpoint: string) {
    return this.http.get(this.url + '/' + endpoint, this.headers);
  }

  post(endpoint: string, body: any) {
    return this.http.post(this.url + '/' + endpoint, body, this.headers);
  }

  put(endpoint: string, body: any) {
    return this.http.put(this.url + '/' + endpoint, body, this.headers);
  }

  delete(endpoint: string) {
    return this.http.delete(this.url + '/' + endpoint, this.headers);
  }

  patch(endpoint: string, body: any) {
    return this.http.put(this.url + '/' + endpoint, body, this.headers);
  }
}
