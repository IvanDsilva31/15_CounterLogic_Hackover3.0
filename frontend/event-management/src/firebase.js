import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyB5EbXk0JzzOjUbno3P3bccZdw5MRpSeVY",
  authDomain: "counterlogic-b88eb.firebaseapp.com",
  databaseURL: "https://counterlogic-b88eb-default-rtdb.firebaseio.com",
  projectId: "counterlogic-b88eb",
  storageBucket: "counterlogic-b88eb.appspot.com",
  messagingSenderId: "1048060140196",
  appId: "1:1048060140196:web:d2f9804086a2066044a431",
  measurementId: "G-PEKM8382TB",
};

const app = initializeApp(firebaseConfig);

const auth = getAuth();

export { app, auth };
