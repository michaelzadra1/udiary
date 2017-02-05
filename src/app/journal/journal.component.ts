import { Component, OnInit } from '@angular/core';
import { Journal }    from './journal';

@Component({
  selector: 'app-journal',
  templateUrl: './journal.component.html'
})
export class JournalComponent implements OnInit {

  journal: Journal;

  constructor() { }

  ngOnInit() {
    this.journal = {
      name: '',
      date: null,
      content: ''
    };
  }
  save(journal: Journal, isValid: boolean) {
    if (isValid) {
      console.log(this.journal);
    }
  }

}
