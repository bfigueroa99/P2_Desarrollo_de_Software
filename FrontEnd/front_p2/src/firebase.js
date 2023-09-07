// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyDM2Xwh8ounvvMyOurV6lyQ4PpmbpJ3y04",
    authDomain: "pdsp2-dc1e0.firebaseapp.com",
    projectId: "pdsp2-dc1e0",
    storageBucket: "pdsp2-dc1e0.appspot.com",
    messagingSenderId: "426350195042",
    appId: "1:426350195042:web:b37b5ab86bc6bea1c5fc3b",
    measurementId: "G-VTF3V05RK2"
};


const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export { auth };