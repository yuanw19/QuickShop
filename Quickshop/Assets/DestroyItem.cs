using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DestroyItem : MovingCamera
{
    private string objectName;
    // Start is called before the first frame update
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {

    }

    void OnMouseDown()
    {
        objectName = gameObject.name;
        addItem(objectName);
        Destroy(gameObject);
    }
}
