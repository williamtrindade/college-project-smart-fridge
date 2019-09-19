<?php

/** @var \Illuminate\Database\Eloquent\Factory $factory */

use App\Transaction;
use Faker\Generator as Faker;

$factory->define(Transaction::class, function (Faker $faker) {
    return [
        'date_time'   => $faker->dateTime(),
        'opcode'      => $faker->randomElement(['RETR', 'STOR']),
        'product_id'  => function () {
            return factory(App\Product::class)->create()->id;
        },
    ];
});
