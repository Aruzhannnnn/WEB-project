export interface Tour{
  id: number;
  name: string;
  country: string;
  price: number;
  description: string;
  image: string;
  like: number;
  descfull: string;
  duration: string;
  inclusions: string;
  exclusions: string;
}

export interface AuthToken{
  token: string;
}
