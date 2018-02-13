import {Component, OnInit} from '@angular/core';

import {Risks} from './providers/services/risks';
import {Router} from '@angular/router';
/**
 * our main component just get all risks for company and draw side nav with risks type names
 */
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  risksTypes = [];

  constructor(private _http: Risks, public _router: Router) {
  }

  ngOnInit() {
    this._http.getAllRisks().subscribe((data) => {
      data['result'].forEach((risk) => {
        this.risksTypes = [
          ...this.risksTypes,
          {id: risk.id, riskName: risk.riskName}
        ];
      });
      if (this.risksTypes[0].id) {
        this._router.navigateByUrl('/risk/' + this.risksTypes[0].id)
      }
    });
  }

  getRisk(id) {
    const p = '/risk/' + id
    this._router.navigateByUrl(p);
  }
}
