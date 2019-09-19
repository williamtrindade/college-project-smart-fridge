<?php

namespace App\Repositories;

use App\Repositories\Contracts\EloquentRepository;
use App\Transaction;

class TransactionRepository implements EloquentRepository
{
    private $model;

    public function __construct(Transaction $model)
    {
        $this->model = $model;
    }

    public function all()
    {
        return $this->model->all();
    }

    public function create($data)
    {
        return $this->model->create($data);
    }

    public function read($id)
    {
        return $this->model->find($id);
    }

    public function update($id, $data)
    {
        return $this->model->save($id, $data);
    }

    public function delete($id)
    {
        return $this->model->delete($id);
    }
}