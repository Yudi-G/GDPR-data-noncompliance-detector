import { Component } from '@angular/core';
import { CommonModule, NgIf } from '@angular/common';
import { RouterModule } from '@angular/router';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-upload-document',
  standalone: true,
  imports: [CommonModule,RouterModule],
  templateUrl: './upload-document.component.html',
  styleUrls: ['./upload-document.component.css']
})
export class UploadDocumentComponent {
  
  isDragActive: boolean = false;
  currentAnalysis: any = {};
  uploadedFileName: string = ''; 
  fileContent: string = '';

  fileName = '';

  constructor(private http: HttpClient) {}

  onFileSelected(event: any) {
    const file: File = event.target.files[0];

    if(file) {
      this.fileName = file.name;
      
      const formData = new FormData();
      formData.append("file", file);

      const upload$ = this.http.post("http://127.0.0.1:8000/file-upload", formData);

      upload$.subscribe();
    }
  }


  isObjectEmpty(obj: any) {
    return Object.keys(obj).length === 0;
  }

  // onFileSelected(event:any) {
  //   const file: File = event.target.files[0];
  //   if (file) {
  //     this.uploadedFileName = file.name;
  //     const reader = new FileReader();
  //     reader.readAsText(file);
  //     reader.onload = () => {
  //       if (reader.result) {
  //         this.fileContent = reader.result.toString();
  //       }
  //     };
  //   }
  // }

  onFileDropped(event: DragEvent) {
    event.preventDefault();
    if (event.dataTransfer) {
      const file = event.dataTransfer.files[0];
      console.log(file);
    }
  }

  onDragOver(event: DragEvent) {
    event.stopPropagation();
    event.preventDefault();
    this.isDragActive = true;
  }

  onDragLeave(event: DragEvent) {
    event.stopPropagation();
    event.preventDefault();
    this.isDragActive = false;
  }
}
