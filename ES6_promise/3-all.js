import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  const promiseA = uploadPhoto();
  const promiseB = createUser();
  return Promise.all([promiseA, promiseB])
    .then((data) => {
      console.log(`${data[0].body} ${data[1].firstname} ${data[1].lastname}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
