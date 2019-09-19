<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Product extends Model
{
    protected $table = 'products';

    protected $fillable = [
        'name', 'amount'
    ];

    /**
     * Return Transactions
     */
    public function transactions()
    {
        return $this->hasMany('App\Products');
    }
}
