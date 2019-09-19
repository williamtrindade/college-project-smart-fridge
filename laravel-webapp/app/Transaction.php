<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Transaction extends Model
{
    protected $table = 'transactions';

    protected $fillable = [
        'datetime', 'opcode'
    ];

    /**
     * Return Product
     */
    public function product()
    {
        return $this->belongsTo('App\Product');
    }
}
