import { Component } from '@angular/core';
import { UsersService } from '../users.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {

  constructor(private userService: UsersService) {}

  onSubmit(form: any) {
    this.userService.register(form.value).subscribe(
      response => {
        console.log('User registered', response);
      },
      error => {
        console.error('Registration failed', error);
      }
    );
  }
}
