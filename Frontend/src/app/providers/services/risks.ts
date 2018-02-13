/**
 * Api is a generic REST Api handler. Set your API url first.
 */
import {Injectable} from '@angular/core';
import {Api} from '../api';


@Injectable()
export class Risks {
  endPoint = 'risk/1/';

  constructor(public api: Api) {
  }

  getAllRisks() {
    return this.api.get(this.endPoint);
  }

  addRiskData(id,data) {
    return this.api.post(this.endPoint + id + '/', data);
  }

  getRisk(id) {
    return this.api.get(this.endPoint + id + '/');
  }
}
