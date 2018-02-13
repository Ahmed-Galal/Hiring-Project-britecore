import {Component, OnInit} from '@angular/core';
import {FormControl, FormGroup} from '@angular/forms';
import {ActivatedRoute} from '@angular/router';
import {Risks} from '../providers/services/risks';
/**
 * this is our dynamic form it hits the api and draw table of risk data
 * and of course you can submit the data
 */
@Component({
  selector: 'app-dynamic-form',
  templateUrl: './dynamic-form.component.html',
  styleUrls: ['./dynamic-form.component.css']
})
export class DynamicFormComponent implements OnInit {
  fieldList = [];
  riskName;
  riskRows;
  form: FormGroup;

  constructor(private _http: Risks, public _route: ActivatedRoute) {
  }

  mapData(riskData) {
    const formGroup = {};
    Object.keys(riskData).forEach((field) => {
      this.fieldList = [...this.fieldList,
        {
          id: riskData[field]['id'],
          key: field,
          label: field,
          // value: riskData[field]['data'],
          type: riskData[field]['type'],
          options: riskData[field]['options'],
          validation: {required: true},
        }];
      // formGroup[field] = new FormControl(riskData[field]['data'] || '');
      formGroup[field] = new FormControl();
    });
    return formGroup
  }

  ngOnInit() {
    if (this._route.snapshot.paramMap.get('id')) {
      debugger;
      this.riskName = this._route.snapshot.paramMap.get('riskName');
      this._http.getRisk(this._route.snapshot.paramMap.get('id')).subscribe((data) => {
        this.riskRows = data['result'];
        let formGroup = this.mapData(data['result'][0]);
        this.form = new FormGroup(formGroup);

      });
    }
  }

  editRisk(row) {
    console.log(row);
  }

  deleteRisk(row) {
    console.log(row);

  }

  onSubmit(form) {
    console.log(form);
    const id = this._route.snapshot.paramMap.get('id');
    this._http.addRiskData(id, form).subscribe((data) => {
        if (data['result'].length > 0) {
          this.riskRows = data['result']
        }

      },
      (err) => {
        console.log(err)
      })
  }
}

