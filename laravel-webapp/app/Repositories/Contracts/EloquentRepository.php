<?php

namespace App\Repositories\Contracts;

interface EloquentRepository
{
    public function all();
    public function create($data);
    public function read($id);
    public function update($id, $data);
    public function delete($id);
}