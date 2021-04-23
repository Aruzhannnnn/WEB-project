import {Tour} from './models';

export const TOURS: Tour[] = [
  {

    id: 1,
    name: 'Full-Day Essential Seoul Tour',
    country: 'Korea',
    price: 97.44,
    description: 'Visit some of Seouls most famous attractions during this 8.5-hour guided tour. Visit Jogye Temple, pass by The Blue House...',
    image: 'https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/09/b8/a0/c8.jpg',
    like: 10,
    descfull: 'Tour the buzzing metropolis of Seoul, South Korea\'s capital, without any hiccups. ' +
      'On this full-day sightseeing tour with entrance fees included, cross the city in air-conditioned comfort' +
      ' with your guide. Take in top attractions including Gyeongbok Palace, Gwanghwamun Gate, ' +
      'and Jogye Temple, and step back in time at the historic Bukchon Hanok Village. ' +
      'There is also an option to add a second day to tour the DMZ.',
    duration: '12h 50m',
    inclusions: 'Local guide • Hotel pickup and drop-off • Transportation to/from attractions by air-conditioned minivan or van',
    exclusions: 'Lunch • Food and drinks, unless specified • Infant meals • Gratuities',
  },
  {
    id: 2,
    name: 'New York in One Day Guided Sightseeing Tour',
    country: 'New York',

    price: 89.00,
    description: 'Tyler is a walking encyclopedia of New York...',
    image: 'https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/07/25/13/74.jpg',
    like: 60,
    descfull: 'Combine New York City’s top attractions in a guided tour via bus and boat (April–December). ' +
      'With insider commentary from your guide, visit Rockefeller Center, South Street Seaport, 9/11 Memorial, ' +
      'and Wall Street. Take a harbor cruise via luxury boat, with views of Ellis Island, the Statue of Liberty, ' +
      'and Brooklyn Bridge. Back on land, hit Lincoln Center and Central Park before wrapping up this whirlwind tour.',
    duration: '6h',
    // tslint:disable-next-line:max-line-length
    inclusions: 'Expert Local Tour Guide Narrative • Transportation With Luxury Tour Bus • Bottled Water on Buses • The Staten Island Ferry',
    exclusions: 'Hotel pickup and drop-off • Lunch • Gratuities',
  },
  {
    id: 3,
    name: 'Private Custom Tour: Tokyo in a Day',
    country: 'Tokyo',
    price: 257.47,
    description: 'Once a small castle town, Tokyo is now one of the world’s most populous and visited cities...',
    image: 'https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/c0/27/38.jpg',
    like: 126,
    descfull: 'Once a small castle town, Tokyo is now one of the world’s most populous and visited cities.' +
      ' Dive deep into the history and culture of this fascinating metropolis during a private,' +
      ' customizable tour of the Japanese capital. ' +
      'From Meiji Shrine—Japan’s most popular Shinto landmark—to the trendy shops of Harajuku, your ' +
      'very own local guide ' +
      'helps you discover incredible sights that suit every taste and time frame.',
    duration: '8h',
    // tslint:disable-next-line:max-line-length
    inclusions: 'Hotel pickup and drop-off (if by private vehicle) • ' +
      'Meet-and-greet service at hotel (if by public transport) • Professional guide ' +
      '• Transport by private vehicle (if by private vehicle) • Transportation fares (if by public transport) • ' +
      'Lunch (full-day option only) • Snacks',
    exclusions: 'Fees for optional tours, activities and lessons • Gratuities',
  },
  {
    id: 4,
    name: 'Intimate Champagne cellar tour - One day out of Paris',
    country: 'Paris',
    price: 371.27,
    description: 'Join two independent french wine guides on an intimate Champagne cellar tour...',
    image: 'https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/3c/80/57.jpg',
    like: 99,
    descfull: 'Clo, who was a winemaker & Clem, who is wine & spirit certified, will take care of you all-day long. \n' +
      '\n' +
      'Because you deserve better than standards, we have selected for you familial wineries, producing some of the finest champagnes. \n' +
      '\n' +
      'You already know about the famous brands so let\'s discover something new and authentic. We want you to discover the best champagne quality, this is why you will taste mostly classified champagnes (grand cru, first cru) and famous local brandies. \n' +
      '\n' +
      'From jewels of French architecture, to picturesque villages : discover history, taste Champagne in the cellars, and pair it with food. In one word, live French!',
    duration: '11h',
    // tslint:disable-next-line:max-line-length
    inclusions: 'Pick up at your hotel • Breakfast : fresh croissants, pains au chocolat, ' +
      'hot coffee & water • Reims cathedral visit • 3 champagne houses - 10 glasses ' +
      '(champagnes and local brandies) • Typical French lunch at the winery paired with champagne • ' +
      'Village and church of Dom Perignon • View point & secret spots • Drop off at your hotel, ' +
      'central Paris or specific address.',
    exclusions: 'Personal expenses during champagne shopping time.',
  },
];
